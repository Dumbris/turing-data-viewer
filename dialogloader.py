import json
from collections import namedtuple
import jinja2

TRAIN_FORMAT = "train"
TEST_FORMAT = "test"
ALICE_ID = 'Alice'
BOB_ID = 'Bob'
USERTYPE_BOT = 'Bot'
USERTYPE_HUMAN = 'Human'

Utt = namedtuple('Utt', ["userid", "usertype", "text"])

def usertype2bool(userType: str) -> bool:
    if userType == USERTYPE_BOT:
        return 1
    return 0

def utt2html(utt: Utt) -> str:
    return "<td class=\"speaker\"><span class=\"speaker {} {}\">{}</span>({}):</td><td class=\"text\">{}</td>".format(
        utt.userid.lower(),
        utt.usertype.lower(),
        utt.userid,
        utt.usertype[0],
        utt.text
    )

def arr2html(arr) -> str:
    if len(arr) > 0:
        return "<table class=\"dialog\"><tr>{}</tr></table>".format("</tr><tr>".join([utt2html(item) for item in arr]))
    return ""

def fixecoding(str_:str) -> str:
    return str_.encode('utf-8', 'surrogateescape').decode('utf-8')

def load_json(file_, format=TRAIN_FORMAT):
    result = []
    dialogId = []
    num_utt = []
    with open(file_, encoding='utf-8') as fh:
        data = json.load(fh)
        for row in data:
            target_alice = None
            target_bob = None
            quality_alice = None
            quality_bob = None
            if format==TRAIN_FORMAT:
                for user in row["users"]:
                    if user["id"] == ALICE_ID:
                        target_alice = user["userType"]
                    if user["id"] == BOB_ID:
                        target_bob = user["userType"]
                for user in row["evaluation"]:
                    if user["userId"] == ALICE_ID:
                        quality_alice = user["quality"]
                    if user["userId"] == BOB_ID:
                        quality_bob = user["quality"]
            thread = []
            for utt in row["thread"]:
                user_type = None
                if utt["userId"] == ALICE_ID:
                    user_type = target_alice
                if utt["userId"] == BOB_ID:
                    user_type = target_bob
                thread.append(Utt(utt["userId"], user_type, jinja2.escape(fixecoding(utt["text"]))))
            result.append({
                'dialogId': row["dialogId"],
                'text': arr2html(thread),
                'quality_alice': quality_alice,
                'quality_bob': quality_bob,
                'context': jinja2.escape(fixecoding(row['context'])),
            })
    return result

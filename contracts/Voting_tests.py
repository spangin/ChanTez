import time
import smartpy as sp

Voting = sp.io.import_script_from_url("https://raw.githubusercontent.com/spangin/ChanTez/main/contracts/Voting.py").Voting

    
##############################################################################

# Tests
@sp.add_test(name = "Voting")
def test():
    CURRENT_TIME = round(time.time())

    userA = sp.test_account("UserA")
    userB = sp.test_account("UserB")
    userC = sp.test_account("UserC")
    scenario = sp.test_scenario()
    scenario.h1("Voting tests")
    voting = Voting(sp.utils.bytes_of_string("What?"),
                    [sp.utils.bytes_of_string("ans21"),
                     sp.utils.bytes_of_string("ans2"),
                     sp.utils.bytes_of_string("ans1")],
                    sp.timestamp(CURRENT_TIME - 60),
                    sp.timestamp(CURRENT_TIME + 60))
    scenario += voting

    voting.vote(1).run(sender=userA, now = sp.timestamp(CURRENT_TIME))
    voting.vote(1).run(sender=userA, amount = sp.tez(1), now = sp.timestamp(CURRENT_TIME), valid = False)
    voting.vote(1).run(sender=userA, now = sp.timestamp(CURRENT_TIME-61), valid = False)
    voting.vote(1).run(sender=userA, now = sp.timestamp(CURRENT_TIME+61), valid = False)
    voting.vote(50).run(sender=userA, valid = False)
    voting.vote(2).run(sender=userA, valid = False)
    voting.vote(3).run(sender=userC)
    voting.vote(1).run(sender=userB)

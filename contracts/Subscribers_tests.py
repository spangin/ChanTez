import smartpy as sp

Subscribers = sp.io.import_script_from_url("https://raw.githubusercontent.com/spangin/ChanTez/main/contracts/Subscribers.py").Subscribers

##############################################################################

# Tests
@sp.add_test(name = "Subscribers")
def test():
    userC = sp.test_account("UserC")
    userA = sp.test_account("UserA")
    userB = sp.test_account("UserB")
    scenario = sp.test_scenario()
    scenario.h1("Subscribers tests")
    subscribers = Subscribers(userC.address)
    scenario += subscribers

    scenario.verify(~subscribers.is_follower(userA.address))
    subscribers.follow(userA.address).run(sender = userC)
    subscribers.follow(userA.address).run(sender = userB, valid = False)
    subscribers.follow(userA.address).run(sender = userC, valid = False)
    scenario.verify(subscribers.is_follower(userA.address))
    subscribers.set_follower_status(address = userA.address, status = 5).run(sender = userC)
    subscribers.set_follower_status(address = userA.address, status = 9).run(sender = userB, valid = False)
    subscribers.set_follower_status(address = userB.address, status = 7).run(sender = userC, valid = False)
    subscribers.unfollow(userB.address).run(sender = userC, valid = False)
    subscribers.follow(userB.address).run(sender = userC)
    subscribers.unfollow(userB.address).run(sender = userA, valid= False)
    subscribers.unfollow(userB.address).run(sender = userC)
    subscribers.unfollow(userB.address).run(sender = userC, valid= False)

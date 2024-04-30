import smartpy as sp

ReactionsLog = sp.io.import_script_from_url("https://raw.githubusercontent.com/spangin/ChanTez/main/contracts/ReactionsLog.py").ReactionsLog

##############################################################################

# Tests
@sp.add_test(name = "ReactionsLog")
def test():
    userC = sp.test_account("UserC")
    userA = sp.test_account("UserA")
    userB = sp.test_account("UserB")
    scenario = sp.test_scenario()
    scenario.h1("ReactionsLog tests")
    reactez = ReactionsLog(userC.address)
    scenario += reactez

    reactez.set_reaction(key = sp.record(u = userA.address, i = 100), value = 1).run(sender = userC)
    scenario.verify(reactez.get_reaction(sp.record(u = userA.address, i = 100)).open_some() == 1)
    reactez.set_reaction(key = sp.record(u = userA.address, i = 100), value = 5).run(sender = userB, valid = False)
    reactez.set_reaction(key = sp.record(u = userA.address, i = 100), value = 7).run(sender = userC)
    reactez.remove_reaction(sp.record(u = userA.address, i = 100)).run(sender = userB, valid = False)
    reactez.remove_reaction(sp.record(u = userA.address, i = 100)).run(sender = userC)

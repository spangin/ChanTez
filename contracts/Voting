import time
import smartpy as sp


class Voting(sp.Contract):

    ERR_INVALID_TX_AMOUNT    = "ERR invalid tx amount"
    ERR_INVALID_TIME         = "ERR invalid time to vote"
    ERR_INVALID_OPTION       = "ERR invalid option"
    ERR_ALREADY_VOTED        = "ERR already voted"

    def __init__(self, q, o, f, t):
        self.init(
            # question
            q = q,
            # options
            o = o,
            # time from
            f = f,
            # time to
            t = t,
            # voters
            v = sp.big_map(tkey = sp.TAddress, tvalue = sp.TNat),
            # result
            r = sp.map(tkey = sp.TNat, tvalue = sp.TNat)
        )

    @sp.entry_point()
    def vote(self, params):
        sp.set_type(params, sp.TNat)
        sp.verify(sp.amount == sp.mutez(0), message = Voting.ERR_INVALID_TX_AMOUNT)
        sp.verify((self.data.f <= sp.now) & (sp.now <= self.data.t), message = Voting.ERR_INVALID_TIME)
        sp.verify((params > 0) & (params <= sp.len(self.data.o)), message = Voting.ERR_INVALID_OPTION)
        sp.verify(~self.data.v.contains(sp.source), message = Voting.ERR_ALREADY_VOTED)
        s = sp.local("s", self.data.r.get(params, default_value = sp.nat(0)))
        self.data.r[params] = s.value + 1
        self.data.v[sp.source] = params

import smartpy as sp


class ReactionsLog(sp.Contract):

    def __init__(self, channel):
        self.init(
            channel = channel,
            reactions = sp.big_map(tkey = sp.TRecord(u = sp.TAddress, i = sp.TNat), tvalue = sp.TInt),
        )


    @sp.onchain_view()
    def get_reaction(self, params):
        sp.result(self.data.reactions.get_opt(params))

    
    @sp.entry_point()
    def set_reaction(self, params):
        sp.set_type(params.key, sp.TRecord(u = sp.TAddress, i = sp.TNat))
        sp.set_type(params.value, sp.TInt)
        sp.verify(self.data.channel == sp.sender, message = "ERR access denied")
        self.data.reactions[params.key] = params.value

    
    @sp.entry_point()
    def set_reactions(self, params):
        sp.set_type(params, sp.TMap(k = sp.TRecord(u = sp.TAddress, i = sp.TNat), v = sp.TInt))
        sp.verify(self.data.channel == sp.sender, message = "ERR access denied")
        sp.for entry in params.items():
            self.data.reactions[sp.record(u = entry.key.u, i = entry.key.i)] = entry.value


    @sp.entry_point()
    def remove_reaction(self, params):
        sp.set_type(params, sp.TRecord(u = sp.TAddress, i = sp.TNat))
        sp.verify(self.data.channel == sp.sender, message = "ERR access denied")
        del self.data.reactions[params]

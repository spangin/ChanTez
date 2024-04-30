import smartpy as sp


class Subscribers(sp.Contract):

    def __init__(self, channel):
        self.init(
            channel = channel,
            total = sp.int(0),
            subscribers = sp.big_map(tkey = sp.TAddress, tvalue = sp.TInt)
        )

    
    @sp.onchain_view()
    def is_follower(self, address):
        sp.result(self.data.subscribers.contains(address))


    @sp.entry_point()
    def set_follower_status(self, params):
        sp.set_type(params.address, sp.TAddress)
        sp.set_type(params.status, sp.TInt)
        sp.verify(self.data.channel == sp.sender, message = "ERR access denied")
        sp.verify(self.data.subscribers.contains(params.address), message = "ERR not found")
        self.data.subscribers[params.address] = params.status
    
    
    @sp.entry_point()
    def follow(self, address):
        sp.set_type(address, sp.TAddress)
        sp.verify(self.data.channel == sp.sender, message = "ERR access denied")
        sp.verify(~self.data.subscribers.contains(address), message = "ERR already done")
        self.data.subscribers[address] = sp.int(0)
        self.data.total += 1


    @sp.entry_point()
    def unfollow(self, address):
        sp.set_type(address, sp.TAddress)
        sp.verify(self.data.channel == sp.sender, message = "ERR access denied")
        sp.verify(self.data.subscribers.contains(address), message = "ERR not found")
        del self.data.subscribers[address]
        self.data.total -= 1


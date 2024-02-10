def account(initial_balance):
    def deposit(amount):
        dispatch['balance'] += amount
        return dispatch['balance']
    def withdraw(amount):
        if amount > dispatch['balance']:
            return 'Insufficient funds'
        dispatch['balance'] -= amount
        return dispatch['balance'] 
       
    dispatch = {'deposit': deposit,
                'withdraw': withdraw,
                'balance': initial_balance}
    return dispatch

def withdraw(account, amount):
    return account['withdraw'](amount)

def deposit(account, amount):
    return account['deposit'](amount)

def check_balance(account):
    return account['balance']

from operator import add, sub, mul, truediv

def converter(c, f):
    """Connect c to f with constraints to convert from Celsius to Fahrenheit."""
    u, v, w, x, y = [connector() for _ in range(5)]
    multiplier(c, w, u)
    multiplier(v, x, u)
    adder(v, y, f)
    constant(w, 9)
    constant(x, 5)
    constant(y, 32)
    

def adder(a, b, c):
    """The constrain that a + b = c."""
    return make_ternary_constraint(a, b, c, add, sub, sub)


def multiplier(a, b, c):
    """The constraint that a * b = c."""
    return make_ternary_constraint(a, b, c, mul, truediv, truediv)


def constant(connector, value):
    """The constant that connector = value."""
    constraint = {}
    connector['set_val'](constraint, value)
    return constraint


def make_ternary_constraint(a, b, c, ab, ca, cb):
    """The constrain that ab(a, b)=c and ca(c, a)=b and cb(c, b)=a."""
    def new_value():
        av, bv, cv = [connector['has_val']() for connector in (a, b, c)]
        if av and bv:
            c['set_val'](constraint, ab(a['val'], b['val']))
        elif cv and av:
            b['set_val'](constraint, ca(c['val'], a['val']))
        elif cv and bv:
            a['set_val'](constraint, cb(c['val'], b['val']))
        
    def forget_value():
        for connector in (a, b, c):
            connector['forget'](constraint)
    
    constraint = {'new_val': new_value, 'forget': forget_value}
    for connector in (a, b, c):
        connector['connect'](constraint)
    
    return constraint


def connector(name=None):
    """A connector between constraints."""
    informant = None
    constraints = []
    def set_value(source, value):
        nonlocal informant
        val = connector['val']
        if val is None:
            informant, connector['val'] = source, value
            if name is not None:
                print(f"{name} = {value}")
            inform_all_except(source, 'new_val', constraints)
        else:
            if val != value:
               print(f"Contradiction detected: {val} vs {value}") 

    def forget_value(source):
        nonlocal informant
        if informant == source:
            informant, connector['val'] = None, None
            if name is not None:
                print(f"{name} is forgotten.")
            inform_all_except(source, 'forget', constraints)
    
    connector = {'val': None,
                 'set_val': set_value,
                 'forget': forget_value,
                 'has_val': lambda: connector['val'] is not None,
                 'connect': lambda source: constraints.append(source)}
    return connector

def inform_all_except(source, message, constraints):
    """Inform all constraints of the message, except source."""
    for c in constraints:
        if c != source:
            c[message]()
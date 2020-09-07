signup = ['first_name', 'last_name', 'username', 'password', 'email', 'phone_no']
login = ['username', 'password']
create_commodity = ['commodity_name', 'buy_sell_date', 'buy_or_sell', 'price']

success_codes = {
    "S100" : "User Created Successfully",
    "S101" : "Login Successful",
    "S102" : "Commodity Entry Created Successfully",
}

error_codes = {

    "E100" : "User Already Exists",
    "E101" : "User not Registered",
    "E102" : "Wrong Username or Password",
    "X100" : "Exception occured while Signup",
    "X101" : "Exception occured while creating commodity entry",
}
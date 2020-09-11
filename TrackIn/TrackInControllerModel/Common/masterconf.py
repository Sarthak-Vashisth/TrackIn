signup = ['first_name', 'last_name', 'username', 'password', 'email', 'phone_no']
login = ['username', 'password']
create_commodity = ['commodity_name', 'buy_sell_date', 'buy_or_sell', 'price']
delete_commodity = ['serial_id']

success_codes = {
    "S100" : "User Created Successfully",
    "S101" : "Login Successful",
    "S102" : "Commodity Entry Created Successfully",
    "S103" : "Commodity Entry Deleted Successfully"
}

error_codes = {

    "E100" : "User Already Exists",
    "E101" : "User not Registered",
    "E102" : "Wrong Username or Password",
    "X100" : "Exception occured while Signup",
    "X101" : "Exception occured while creating commodity entry",
    "X102" : "Exception occured while deleting commodity entry"
}
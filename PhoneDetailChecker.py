import phonenumbers
from phonenumbers import geocoder,carrier

phone_number=input("Enter Mobile No With Country Code:")
Parsed_MobileNum=phonenumbers.parse(phone_number)
Location=geocoder.description_for_number(Parsed_MobileNum,"en")
Service_Provider=carrier.name_for_number(Parsed_MobileNum,"en")
name_phonenum=phonenumbers.is_valid_number(Parsed_MobileNum)
print(f"Location: {Location}")
print(f"Service Provider: {Service_Provider}")
print(f"Valid Number : {name_phonenum}")

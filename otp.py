import random
# if there is a database fetch recent OTP codes from DB and populate otpees array
otpees = []

# create a function that generates random otp of any lenght
def otpGenerator(length):
    otp = []
    for x in range(length):
      otp.append(str(int(random.random() * 10)))
    # print(otp)
    curOTP = ''.join(otp)
    otpees.append(curOTP)
    return curOTP


print("welcome to Random OTP Generator")
length = input('How Many digits do you want the otp to have')
print(otpGenerator(int(length)))
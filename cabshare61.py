#building a dynamic system where cars and autos can be shared by people
dest = ["bhopal","sehore","indore","jabalpur","sehore"]
person=["aditya","dev","shristi","augustya","frank"]
phone =["1234567890","1234567890","1234567890","8982076323","1234567890"]
time=["11am","6pm","2am","9pm","4am"]

for l in range(4):
	
	lendes=len(dest)
	destcount=0

	print("Hello, this is the collective cab sharing system. ")
	input2 = int(input("press 1 to upload your cab share and press 2 to view available cabs (or press 999 to exit) "))
	if input2 == 2:
		destination = input("please go ahead and enter your destination. ")
		destinationlower=destination.lower()
		for i in range(lendes):
			if dest[i]==destinationlower:
				destcount=destcount+1
				print("destination: ",dest[i])
				print("person sharing the cab: ",person[i])
				print("phone number of the driver: ",phone[i])
				print("time of cab departure: ",time[i])
				print()
	
		if destcount==0:
			print(f"no cabs found that go to {destination}")
	elif input2==1:
		desti=input("what destination?")
		pers=input("enter the name of the person sharing the cab")
		phon=input("enter the driver's contact number")
		tim=input("at what time?")
		destilower=desti.lower()
		perslower=pers.lower()
		phonlower=phon.lower()
		timlower=tim.lower()
		
		dest.append(destilower)
		person.append(perslower)
		phone.append(phonlower)
		time.append(timlower)
		print("your entry has been sucessfully added to the system")

	elif input2==999:
		break
	else:
		print("input not recognised please try again.")
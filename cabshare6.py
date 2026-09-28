#building a dynamic system where cars and autos can be shared by people
dest = ["bhopal","sehore","indore","jabalpur","sehore"]
person=["aditya","dev","shristi","augustya","frank"]
phone =["9875412365","7569842315","6587936547","8982075893","9875625874"]
time=["11am","6pm","2am","9pm","4am"]

for l in range(4):
	
	lendes=len(dest)
	destcount=0 #destcount will help us see if a cab really goes to that destination

	print("Hello, this is the collective cab sharing system. ")
	input2 = int(input("press 1 to upload your cab share and press 2 to view available cabs (or press 999 to exit) "))
	if input2 == 2:
		destination = input("please go ahead and enter your destination. ")
		for i in range(lendes):
			if dest[i]==destination:
				destcount=destcount+1
				print("destination: ",dest[i])
				print("person sharing the cab: ",person[i])
				print("phone: ",phone[i])
				print("time of cab departure: ",time[i])
				print()
	
		if destcount==0:
			print(f"no cabs found that go to {destination}")
	elif input2==1:
		desti=input("what destination?")
		pers=input("enter person name")
		phon=input("enter the persons contact number")
		tim=input("at what time?")

		dest.append(desti)
		person.append(pers)
		phone.append(phon)
		time.append(tim)
		print("your entry has been sucessfully added to the system")

	elif input2==999:
		break
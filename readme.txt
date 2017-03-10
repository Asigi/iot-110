NOTE: 
	- On the Mac computer: 
		- arshdeep/Documents/3rd_mount is linked to:
			- raspPi’s Documents/3rd_mount

	SSHFS from within the mac’s Document folder (Don’t go into any deeper folders).
		sshfs pi@iot9090.local:Documents/3rd_mount 3rd_mount/ -C
		
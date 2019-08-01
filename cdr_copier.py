import os, glob
import time
import shutil
from ftplib import FTP


def cdr_download_from_ftp(day):
        """CDR Download from 10.10.10.10"""
        # FTP Credentials
        ip = "10.10.10.10"
        username = 'ftp_username'
        password = 'ftp_password'

        #changes the active dir - this is where downloaded files will be saved
        os.chdir("C:\Users\Administrator\Desktop\cdr_copy_demo")
        
        # Login to Switch
        try:
                ftp = FTP(ip)
                ftp.login(username,password)
                print("\nLogin Successfull for Switch...\n")
        except Exception as err:
                print(err)

        ftp.cwd("/cdr/ICDR/secondary") #files downloaded from ftp directory

        count = 0
        files = ftp.nlst() #getting all cdr files from ftp
        reverse_list = files[-1200:] #reverse list for getting latest cdr first

        if day == 1:
                for i in range(len(reverse_list)):
                        if reverse_list[i][16:24] == input_date_list[0]:
                                count += 1
                                print("Found cdr: " + reverse_list[i])
                                print("Starting to download: " + reverse_list[i])
                                try:
                                        ftp.retrbinary("RETR " + reverse_list[i], open(reverse_list[i], 'wb').write)
                                        print("Download Complete: " + reverse_list[i])
                                        print("\n")
                                except Exception as err:
                                        print(err)
                ftp.close()
                cdr = "Total Downloaded CDR for " + input_date_list[0] + " = "

        elif day == 2:
                for i in range(len(reverse_list)):
                        if (reverse_list[i][16:24] == input_date_list[0] or
                                reverse_list[i][16:24] == input_date_list[1]):

                                count += 1
                                print("Found cdr: " + reverse_list[i])
                                print("Starting to download: " + reverse_list[i])
                                try:
                                        ftp.retrbinary("RETR " + reverse_list[i], open(reverse_list[i], 'wb').write)
                                        print("Download Complete: " + reverse_list[i])
                                        print("\n")
                                except Exception as err:
                                        print(err)
                ftp.close()
                cdr = "Total Downloaded CDR for " + input_date_list[0] + " to " + input_date_list[1] + " = "

        elif day == 3:
                for i in range(len(reverse_list)):
                        if (reverse_list[i][16:24] == input_date_list[0] or
                                reverse_list[i][16:24] == input_date_list[1] or
                                reverse_list[i][16:24] == input_date_list[2]):

                                count += 1
                                print("Found cdr: " + reverse_list[i])
                                print("Starting to download: " + reverse_list[i])
                                try:
                                        ftp.retrbinary("RETR " + reverse_list[i], open(reverse_list[i], 'wb').write)
                                        print("Download Complete: " + reverse_list[i])
                                        print("\n")
                                except Exception as err:
                                        print(err)
                ftp.close()
                cdr = "Total Downloaded CDR for " + input_date_list[0] + " to " + input_date_list[2] + " = "

        if count == 0:
                cdr = "No CDR found for " + input_date_list[0]
                print("{}".format(cdr))                 
        else:
                print("{} {}".format(cdr, count))
        
        print("\n")

def cdr_upload_to_ftp():
        """CDR uploaded to 172.22.21.11 from local Machine"""        
        # FTP Credentials
        ip = '172.22.21.11'
        username = 'ftp_username'
        password = 'ftp_password'

        # IOF FTP Login
        try:
                ftp = FTP(ip)
                ftp.login(username,password)
                print("\nLogin Successfull for IOF FTP...\n")
        except Exception as err:
                print(err)
        
        ftp.cwd('/') #IOF FTP path
        count = 0
        for root, dir, files in os.walk('C:\Users\Administrator\Desktop\cdr_copy_demo'):
                for fname in files:
                        full_fname = os.path.join(root, fname)
                        print("Starting to upload: " + fname)
                        count += 1
                        try:
                                ftp.storbinary('STOR ' + fname, open(full_fname, 'rb'))
                                print("Upload Complete: " + fname)
                                print("\n")
                        except Exception as err:
                                print(err)     

        ftp.close()
        cdr = "Total Uploaded CDR " + " = "
        print("{} {}".format(cdr, count))

if __name__ == "__main__":
        source_dir = 'C:\Users\Administrator\Desktop\cdr_copy_demo'
        dest_dir = 'C:\Users\Administrator\Desktop\cdrtemp'

        print("\nMoving files to cdrdtemp folder...wait\n")
        for filename in glob.glob(os.path.join(source_dir, '*.*')):
                shutil.move(filename, dest_dir)

        time.sleep(2)

        n = int(input("Input Number of Recent days (Max 1 to 3) for uploading/downloading CDR: "))
        i = 1
        input_date_list = []
        if (n >= 1 and n <= 3):
                while i <= n:
                        input_date = str(input("\nType Date YYYYMMDD Format:"))
                        input_date_list.append(input_date)
                        i += 1
                cdr_download_from_ftp(len(input_date_list))
                time.sleep(5)
                # cdr_upload_to_ftp()
        else:
                print("\nInvalid Date Input...")

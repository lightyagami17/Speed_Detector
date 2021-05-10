#Install the following extension/library
#pip install speedtest-cli

print('Author : Abhishek Tenneti') #Here, you can add your name/credentials 
print('Wi-Fi Name: Your-Wifi Name') # Here, give the name of your Internet Connection and details. 


from speedtest import Speedtest
st = Speedtest()
a = (st.download())/1000000
b = (st.upload())/1000000

print('Download Speed :',a,'Mbps') # This converts the speed into Mbps the standard measure of speed
print('Upload Speed :',b,'Mbps')

st.get_servers([])
print('Ping (in ms) :',st.results.ping)

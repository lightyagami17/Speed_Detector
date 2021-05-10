#Install the following extension/library
#pip install speedtest-cli

print('Author : Abhishek.Tenneti')
print('Wi-Fi Name: tsr')


from speedtest import Speedtest
st = Speedtest()
a = (st.download())/1000000
b = (st.upload())/1000000

print('Download Speed :',a,'Mbps')
print('Upload Speed :',b,'Mbps')

st.get_servers([])
print('Ping (in ms) :',st.results.ping)

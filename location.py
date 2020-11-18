import plotly.express as px
import plotly.graph_objects as go


location_dict = {
	'cctv1' : [28.608177, 77.216060,'Suspect Location : TN02AB1234 : 5.34 PM '],
	'cctv2' : [28.610358, 77.212281,'Location 2'],
	'cctv3' : [28.609293, 77.209213,'Location 3'],
	'cctv4' : [28.610612, 77.205984,'Location 4'],
	'cctv5' : [28.611203, 77.199300,'Location 5'],
	'cctv6' : [28.605193, 77.198885,'Location 6'],
	'cctv7' : [28.602480, 77.193832,'Location 7'],
	'cctv8' : [28.605993, 77.187534,'Location 8'],

	'cctv9' : [28.584076, 77.151148,'Location 9'],
	'cctv10' : [28.582371, 77.154195,'Location 10'],
	'cctv11' : [28.583068, 77.149614,'Location 11'],
	'cctv12' : [28.579083, 77.148208,'Location 12'],
	'cctv13' : [28.579262, 77.146974,'Location 13'],
	
	'cctv14' : [28.572088, 77.161989,'Location 14'],
	'cctv15' : [28.578564, 77.175980,'Location 15'],
	'cctv16' : [28.570217, 77.184863,'Location 16'],
	'cctv17' : [28.565802, 77.181598,'Location 17'],
	'cctv18' : [28.562415, 77.188702,'Location 18']
}


filename = "cctv1_1.png"

loc = location_dict[filename.split('_')[0]]

print(loc)

fig = px.scatter_mapbox(lat=[i[0] for i in location_dict.values()][:8], lon=[i[1] for i in location_dict.values()][:8], hover_name=[i[2] for i in location_dict.values()][:8],
                        color_discrete_sequence=["red"]*8, zoom=14, height=900, size=[20]*8)



# fig = go.Figure(data=go.Scattermapbox(
#         lon = [loc[1],location_dict['cctv2'][1]],
#         lat = [loc[0],location_dict['cctv2'][0]],
#         text = ['Heloo',"dfv"],
#         mode = 'markers+lines',
#         marker_color = ['blue'], 
#         ))

fig.update_layout(mapbox_style="streets", mapbox_accesstoken="pk.eyJ1IjoicmFodWxyazIzMDMiLCJhIjoiY2tkZDhka2dyMDl1ODJ3bnIyMGIza2wxZCJ9.zlNfmSZyo5K3KcGEvclZ-A")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
import plotly
plotly.offline.plot(fig, filename='file.html')
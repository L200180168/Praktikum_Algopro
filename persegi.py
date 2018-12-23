ddef hitung_luas():
    "fungsi menghitung PERSEGI"
    s = 5
    luas = s * s
    return luas
print "<!DOCTYPE html>"
print
print """<html>
	<head>
		<title>Luas Persegi</title>
	</head>
	<body>
		<form>
			<table>
				<tr>
					<td rowspan='8'>
					<img src='../persegi.png' width='150' height='150'>
					</td>
					<td>
						<p><b><font size='5'>Bangun Geometri</font></b></p>
					</td>
				</tr>
				
				<tr>
					<td>Nama Bangun</td>
					<td>:</td>
					<td>Persegi</td>
				</tr>
				
				<tr>
					<td>Dimensi</td>
					<td>:</td>
					<td>2D</td>
				</tr>
				
				<tr>
					<td>Rumus Luas</td>
					<td>:</td>
					<td>Sisi x Sisi</td>
				</tr>
				
				<tr>
					<td>Sisi</td>
					<td>:</td>
					<td>
					5
					</td>
				</tr>
				
    
				<tr>
					<td>Luas</td>
					<td>:</td>
					<td>"""
print persegi()
print"""</td>
				</tr>
			</table>
		</form>
	</body>
</html>"""

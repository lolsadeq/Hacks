using System;
using System.IO;
using System.Drawing;
using System.Runtime.Serialization;
using System.Runtime.Serialization.Formatters;
using System.Runtime.Serialization.Formatters.Binary;
using System.Collections.Generic;

public class MyClass
{
	public static void Main()
	{
//		Font f1 = new Font("Arial", 12);
//		Font f2 = new Font("Verdana", 12, FontStyle.Bold);
		Font f3 = new Font("Lucida Console", 14, FontStyle.Italic);
		
//		WL(f1.ToString());
//		WL(f2.ToString());
		WL("Created Font");
		WL(f3.ToString());
		
//		TextWriter tw = new StreamWriter("config.xml");
//		XmlSerializer xs = new XmlSerializer(f1.GetType());
//		xs.Serialize(tw, f1);	

		WL("Serialize Font");
		try {
			Stream s = File.OpenWrite(@"c:\binaryfile.bin");
			IFormatter f = new BinaryFormatter();
			f.Serialize(s, f3);
			s.Close();
		} catch (Exception e) {
			WL(e.Message);
			WL(e.InnerException.ToString());
		}
		
		WL("Deserialize Font");
		try {
			Stream s = File.OpenRead(@"c:\binaryfile.bin");
			IFormatter f = new BinaryFormatter();
			Font ff = (Font)f.Deserialize(s);
			s.Close();
			WL(ff.ToString());
		} catch (Exception e) {
			WL(e.Message);
			WL(e.InnerException.ToString());
		}
		
		RL();
	}
	
	#region Helper methods

	private static void WL(object text, params object[] args)
	{
		Console.WriteLine(text.ToString(), args);	
	}
	
	private static void RL()
	{
		Console.ReadLine();	
	}
	
	private static void Break() 
	{
		System.Diagnostics.Debugger.Break();
	}

	#endregion
}

using System;

namespace SwitchExpressionSample {
	
	class MainClass {
		public static void Main (string[] args) {
			Console.WriteLine (GetRGBComponent (0x336699, Color.Red));
			Console.WriteLine (GetRGBComponent (0x336699, Color.Green));
			Console.WriteLine (GetRGBComponent (0x336699, Color.Blue));
		}
		
        // given an int and the color value desired, it returns that color value in 
        // decimal format. Great for breaking down those pesky HTML color values like
        // #003366. e.g. pass it 0x336699 and Color.Red and it returns 51 ...
        // this is achieved by creating an extension method on the Color enum.
        // Who said that enums could not have methods?
		public static int GetRGBComponent(int hex, Color color) {
			return hex >> color.Switch(Red: 16, Green: 8, Blue: 0) & 0xFF;
		}
	}
	
	enum Color { Red, Green, Blue }
	
    // extension methods can also apply to enums
	static class ColorExtensions {
		public static T Switch<T>(this Color color, T Red, T Green, T Blue) {
			switch (color) {
				case Color.Red: return Red;
				case Color.Green: return Green;
				case Color.Blue: return Blue;
				default:
					throw new Exception("Inexhaustive switch");
			}
		}
	}
}
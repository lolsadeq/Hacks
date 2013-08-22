using System;
using System.Linq;
using System.Numerics;
using System.Collections.Generic;

public static class Extensions {

		/// <summary>
		/// Strip the specified args from the specified str. When args is null it 
		/// defaults to stripping all whitespace.
		/// </summary>
		/// <param name='str'>
		/// String: the string to strip
		/// </param>
		/// <param name='args'>
		/// Arguments: a set of characters to strip from str. Expects a string.
		/// </param>
		public static string Strip(this string str, string args = null) {
			if (args == null) {
				return str.Where(c => !char.IsWhiteSpace(c)).JoinAsString();
			} else {
				return str.Where(c => !args.Contains(c)).JoinAsString();
			}
		}
        
}
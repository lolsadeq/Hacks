using System;
 
namespace bittest {
    // test if a bit is set in a byte and some 
    // bit masking antics
    class Program {
        public static void Main(string[] args) {
            while (true) {
                WL(""); W("Enter a number [0-255]: ");
 
                int i = Int32.Parse(RL());
                string sbin = Dec2Bin(i);
                byte b = (byte)i;
 
                WL(""); WL(SF("{0} in binary is {1}. It has {2} bit(s)",
                              new object[] {i, sbin, sbin.Length}));
                WL(""); W("What bit do you want to check: ");
 
                int pos = Int32.Parse(RL());
 
                WL(""); WL(SF("Bit {0} is {1}set!",
                              new object[] {pos, IsBitSet(b, pos) ? "" : "not "}));
                WL(""); W("Continue [Y/n]: ");
 
                if (RL() == "n")
                    break;
            }
        }
 
        static Func<int, string> Dec2Bin = 
            value => Convert.ToString(value, 2);
        static Func<byte, int, bool> IsBitSet = 
            (b, pos) => (b & (1 << pos)) != 0;
 
        static Action<object> W = o => Console.Write(o);
        static Action<object> WL = o => Console.WriteLine(o);
        static Func<string> RL = () => Console.ReadLine();
        static Func<string, object[], string> SF = 
            (frmt, obj) => String.Format(frmt, obj);
    }
}
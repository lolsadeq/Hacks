using System;
using System.Timers;

namespace termtimer {

    class MainClass {

        // Very cool little trick to get a timer to update in place on the console.
        // it uses a carriage return to go back and write over the previous string
        public static void Main(string[] args) {
            Timer t = new Timer();
            t.Elapsed += new ElapsedEventHandler(t_Elapsed);
            t.Interval = 1000;
            t.Start();

            // break and exit when the user enters `Q`
            while (Console.Read() != 'Q') { ; }
        }

        private static void t_Elapsed(object sender, ElapsedEventArgs eea) {
            Console.Write("\r{0}", DateTime.Now);
        }
    }
}

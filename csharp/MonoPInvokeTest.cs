using System;
using System.Runtime.InteropServices;

namespace PidTest {
    class MainClass {

        [DllImport("libc")]
        private static extern int getpid();

        // Using PInvoke in Mono works basically the same as in Windows.
        //   except that Windows native libraries won't be available so you
        //   have to use the equivalent Linux ones.
        public static void Main(string[] args) {
            Console.WriteLine("My PID is: " + getpid().ToString());
        }
    }
}

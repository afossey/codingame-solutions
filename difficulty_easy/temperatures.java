import java.util.*;
import java.io.*;
import java.math.*;

// https://www.codingame.com/ide/puzzle/temperatures

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
class Solution {

    public static void main(String args[]) {
       
        int chosen = 0;
        Scanner in = new Scanner(System.in);
        int n = in.nextInt(); // the number of temperatures to analyse
        for (int i = 0; i < n; i++) {
            
            int t = in.nextInt(); // a temperature expressed as an integer ranging from -273 to 5526
         
            if(chosen == 0) {
                chosen = t;
            } else if(Math.abs(t) == Math.abs(chosen)) {
                chosen = t > 0 ? t : chosen;
            } else if (Math.abs(t) < Math.abs(chosen)){
                chosen = t;
            }
        }

        System.out.println(chosen);
    }
}

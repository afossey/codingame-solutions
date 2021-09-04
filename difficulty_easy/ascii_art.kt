import java.util.*
import java.io.*
import java.math.*

// https://www.codingame.com/ide/puzzle/ascii-art

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
fun main(args : Array<String>) {
    val input = Scanner(System.`in`)
    val L = input.nextInt()
    val H = input.nextInt()
    if (input.hasNextLine()) {
        input.nextLine()
    }
    val T = input.nextLine()

    val alphaBet = "abcdefghijklmnopqrstuvwxyz";

    var result = ""


    for (i in 0 until H) {
        val ROW = input.nextLine()

        val getNewChainWithAddedChar = { res: String, index: Int ->
            res + ROW.substring(index * L, index * L + L)
        }

        for(character in T) {
            val index = alphaBet.indexOf(char = character, ignoreCase = true)
            if(index == -1) {
                result = getNewChainWithAddedChar(result, 26);
            } else {
                result = getNewChainWithAddedChar(result, index)
            }
        }
        result += '\n'
    }

    // Write an action using println()
    // To debug: System.err.println("Debug messages...");

    println(result.toString())
}

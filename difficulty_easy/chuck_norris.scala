import math._
import scala.util._

// https://www.codingame.com/ide/puzzle/chuck-norris

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
object Solution extends App {
    
    def encode(binaryString: String): String = {
      var lastVisited: Option[Char] = None
      
      (0 until binaryString.length).map( i => {
        val currentChar = binaryString.charAt(i)
        if (i == 0) {
          lastVisited = Some(currentChar)
          getNewBlock(currentChar)
        } else {
          if (lastVisited.contains(currentChar)) {
            "0"
          } else {
            lastVisited = Some(currentChar)
            " " + getNewBlock(currentChar)
          }
        }
      }).mkString
    }

  def getNewBlock(currentChar: Char) = currentChar match {
      case '0' => "00 0"
      case _ => "0 0"
  }
  
  def leftPad(str: String, padChar: Char, length: Int): String = {
      (0 until (length - str.length)).map(i => padChar).mkString + str
    }
  
    val message = readLine
    val binary = message.map(char => char.toInt)
        .map(ascii => ascii.toBinaryString)
        .map(str => leftPad(str, '0', 7))
        .mkString
    // Write an action using println
    // To debug: Console.err.println("Debug messages...")
    
    println(encode(binary))
    
}

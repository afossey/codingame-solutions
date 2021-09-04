import java.util.*;
import java.io.*;
import java.math.*;

// https://www.codingame.com/ide/puzzle/power-of-thor-episode-1

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 * ---
 * Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.
 **/
class Player {
    

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int lightX = in.nextInt(); // the X position of the light of power
        int lightY = in.nextInt(); // the Y position of the light of power
        int initialTX = in.nextInt(); // Thor's starting X position
        int initialTY = in.nextInt(); // Thor's starting Y position
        Position target = new Position(lightX, lightY);
        Thor thor = new Thor(initialTX, initialTY, target);
        // game loop
        while (true) {
            int remainingTurns = in.nextInt(); // The remaining amount of turns Thor can move. Do not remove this line.
            thor.moveTowardsTarget();
            // Write an action using System.out.println()
            // To debug: System.err.println("Debug messages...");
            System.err.println("Remaining turns = " + remainingTurns);
           
        }
    }
}

class Thor {
    
    public Position p;
    public Position target;
    
    Thor(int initialX, int initialY, Position target) {
        this.p = new Position(initialX, initialY);
        this.target = target;
    }
    
    public void moveTowardsTarget() {
        int verticalDiffAbs = Math.abs(target.y - p.y);
        int horizontalDiffAbs = Math.abs(target.x - p.x);
        if(verticalDiffAbs > horizontalDiffAbs) {
            moveVertical();
        } else if(verticalDiffAbs < horizontalDiffAbs){
            moveHorizontal();
        } else {
            moveAngle();
        }
    }
    
    public void moveVertical() {
        if(target.y > p.y) {
            moveDown();
        } else if(target.y < p.y) {
            moveUp();
        }
    }
    
    public void moveHorizontal() {
        if(target.x > p.x) {
            moveRight();
        } else if(target.x < p.x) {
            moveLeft();
        }
    }
    
    public void moveUp() {
        System.out.println("N");
        this.p.y--;
    }
    
    public void moveDown() {
        System.out.println("S");
        this.p.y++;
    }
    
    public void moveLeft() {
        System.out.println("W");
        this.p.x--;
    }
    
    public void moveRight() {
        System.out.println("E");
        this.p.x++;
    }
    
    public void moveUpRight() {
        System.out.println("NE");
        this.p.y--;
        this.p.x++;
    }
    
    public void moveUpLeft() {
        System.out.println("NW");
        this.p.y--;
        this.p.x--;
    }
    
    public void moveDownRight() {
        System.out.println("SE");
        this.p.x++;
        this.p.y++;
    }
    
    public void moveDownLeft() {
        System.out.println("SW");
        this.p.x--;
        this.p.y++;
    }
    
    public void moveAngle() {
        int verticalDiff = target.y - p.y;
        int horizontalDiff = target.x - p.x;
        if(verticalDiff > 0 && horizontalDiff > 0) {
            moveDownRight();
        } else if(verticalDiff < 0 && horizontalDiff > 0) {
            moveUpRight();
        } else if(verticalDiff > 0 && horizontalDiff < 0) {
            moveDownLeft();
        } else if(verticalDiff < 0 && horizontalDiff < 0) {
            moveUpLeft();
        }
    }
    
}

class Position {
    int x;
    int y;
    static final int LIMITX = 39;
    static final int LIMITY = 17;
    Position(int x, int y) {
        this.x=x;
        this.y=y;
    }
}

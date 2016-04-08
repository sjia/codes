import org.python.core.*;

public class Point extends PyObject
{
    private int x;
    private int y;

    public Point()
    {
        x = 0;
        y = 0;
    }

    public Point(int x, int y)
    {
        this.x = x;
        this.y = y;
    }

    public void dump()
    {
        System.out.printf("The position is (%s, %s)\n", x , y);
    }
}

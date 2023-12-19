using System;

public class Tetris
{
    private static Tetris instance;

    private Tetris()
    {

    }

    public static Tetris Instance
    {
        get
        {
            if (instance == null)
            {
                instance = new Tetris();
            }
            return instance;
        }
    }


    public void StartGame()
    {
        Console.WriteLine("Гра почалася!");
    }
}

class Program
{
    static void Main()
    {
        Tetris tetris = Tetris.Instance;

        tetris.StartGame();
    }
}

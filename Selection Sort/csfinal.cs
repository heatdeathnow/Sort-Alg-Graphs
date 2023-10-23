using System.Diagnostics;
using static System.Console;

void Shuffle<T>(T[] array){
    Random random = new Random();

    for (int i = array.Length - 1; i > 0; i--){
        int j = random.Next(0, i + 1);
        T temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
}  // This was copied from Chat GPT

void SelectionSort(int[] toSort, int size)
{
    int temp;

    for (int i = 0; i < size - 1; i++)
    {
        int minPos = i;
        for (int j = i + 1; j < size;  j++)
        {
            if (toSort[j] < toSort[minPos])
            {
                minPos = j;
            }
        }

        temp = toSort[i];
        toSort[i] = toSort[minPos];
        toSort[minPos] = toSort[i];
    }
}

void GetPerf(int size, int amount)
{
    Stopwatch stopwatch = new();  // This comes from System.Diagnostics and allows the program to measure time.
    int[] toSort = new int[size];  // Creates the array
    int elapsedTime;  // Milliseconds passed through one round.
    int totalTime = 0;  // Total of milliseconds passed throughout the entire program.
    int worstCase = 0;
    int bestCase = 0;

    for (int i = 0; i < size; i++) { toSort[i] = i; }  // Adds stuff to the array

    for (int i = 0; i < amount; i++)
    {
        Shuffle(toSort);

        stopwatch.Start();
        SelectionSort(toSort, toSort.Length);
        stopwatch.Stop();

        elapsedTime = (int) stopwatch.ElapsedMilliseconds;

        if (i == 0)
        {
            worstCase = elapsedTime;
            bestCase = elapsedTime;
        }

        else if (elapsedTime > worstCase)
        {
            worstCase = elapsedTime;
        }

        else if (elapsedTime < bestCase)
        {
            bestCase = elapsedTime;
        }

        totalTime += elapsedTime;
    }

    Clear();
    WriteLine(@$"Analysis of time taken to sort {amount} lists of size {size}.
    Mean time: {(float) totalTime / 1000 / amount:F2} seconds.
    Best case scenario: {(float) bestCase / 1000:F2} seconds.
    Worst case scenario: {(float) worstCase / 1000:F2} seconds.");
}

// Start of the program.
bool correct = false;
int amount = 0;
int size = 0;

while (!correct && size <= 0) {
    Clear();
    WriteLine("Enter the size of the lists to be sorted.");
    correct = int.TryParse(ReadLine(), out size);
}

correct = false;
while (!correct && amount <= 0) {
    Clear();
    WriteLine("Enter the amount of lists to be sorted.");
    correct = int.TryParse(ReadLine(), out amount);
}

GetPerf(size, amount);
ReadLine();

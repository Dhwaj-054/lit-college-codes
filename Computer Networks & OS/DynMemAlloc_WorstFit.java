//This is Dynamic Memory Allocation in Operating Systems 
// Worst fit method code in Java

import java.util.Scanner;

public class WorstFitMemoryManagement {
    public static void main(String[] args) {
        final int max = 25;
        int[] frag = new int[max];
        int[] b = new int[max];
        int[] f = new int[max];
        int[] bf = new int[max];
        int[] ff = new int[max];
        int nb, nf, temp, highest = 0;

        Scanner sc = new Scanner(System.in);

        System.out.println("\n\tMemory Management Scheme - Worst Fit");

        System.out.print("Enter the number of blocks: ");
        nb = sc.nextInt();

        System.out.print("Enter the number of files: ");
        nf = sc.nextInt();

        System.out.println("\nEnter the size of the blocks:-");
        for (int i = 1; i <= nb; i++) {
            System.out.print("Block " + i + ": ");
            b[i] = sc.nextInt();
        }

        System.out.println("Enter the size of the files :-");
        for (int i = 1; i <= nf; i++) {
            System.out.print("File " + i + ": ");
            f[i] = sc.nextInt();
        }

        for (int i = 1; i <= nf; i++) {
            highest = -1;
            for (int j = 1; j <= nb; j++) {
                if (bf[j] != 1) {
                    temp = b[j] - f[i];
                    if (temp >= 0 && temp > highest) {
                        ff[i] = j;
                        highest = temp;
                    }
                }
            }
            frag[i] = highest;
            bf[ff[i]] = 1;
        }

        System.out.println("\nFile_no:\tFile_size :\tBlock_no:\tBlock_size:\tFragement");
        for (int i = 1; i <= nf; i++) {
            System.out.println(i + "\t\t" + f[i] + "\t\t" + ff[i] + "\t\t" + b[ff[i]] + "\t\t" + frag[i]);
        }

        sc.close();
    }
}




/*Output:

	Memory Management Scheme - Worst Fit
Enter the number of blocks: 5
Enter the number of files: 4

Enter the size of the blocks:-
Block 1: 100
Block 2: 500
Block 3: 200
Block 4: 300
Block 5: 600
Enter the size of the files :-
File 1: 212
File 2: 417
File 3: 112
File 4: 426

File_no:	File_size :	Block_no:	Block_size:	Fragement
1		212		5		600		388
2		417		2		500		83
3		112		4		300		188
4		426		0		0		-1
  */

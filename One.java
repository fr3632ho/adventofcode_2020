import java.util.*;
import java.io.*;

public class One {
  private static int sum = 2020;

  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    ArrayList<Integer> l = new ArrayList<>();
    int q;
    while (scan.hasNext()){
      q = Integer.parseInt(scan.next());
      l.add(q);
    }

    sol1(l);
    sol2(l);

  }

  public static void sol2(ArrayList<Integer> l) {
    Collections.sort(l);

    int n = l.size();
    for (int i=0;i<n-1;i++){
      int low, high, curr;
      low = i+1 % n;
      high = n-2;
      curr = l.get(i);
      while (high > low) {
        int a, b;
        a = l.get(low);
        b = l.get(high);
        if (curr + a + b == sum) {
          System.out.println(curr*a*b);
          return;
        } else if (curr + a + b > sum) {
          high--;
        } else {
          low++;
        }
      }
    }
  }

  public static void sol1(ArrayList<Integer> l) {
    int n = l.size();
    HashSet<Integer> S = new HashSet<>(l);
    for (Integer i : l) {
      int new_sum = sum - i;
      for (Integer j : l) {
        if (S.contains(new_sum - j)){
          System.out.println(i*j*(new_sum - j));
          return;
        }
      }
    }
    }

}

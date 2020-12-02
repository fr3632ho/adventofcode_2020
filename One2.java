import java.util.*;
import java.io.*;

public class One {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    ArrayList<Integer> l = new ArrayList<>();
    HashSet<Integer> s = new HashSet<>();
    int q;
    int sum = 2020;
    while (scan.hasNext()){
      q = Integer.parseInt(scan.next()); // query
      s.add(sum - q);
      l.add(q);
    }

    for (Integer i : l) {
      if (s.contains(i)) {
        System.out.println(i * (sum - s.get(i)));
        System.exit(0);
      }
    }
  }
}

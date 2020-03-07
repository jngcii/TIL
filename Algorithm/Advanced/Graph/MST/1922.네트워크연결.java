import java.util.*;

class Edge {
    int to, cost;
    Edge(int to, int cost) {
        this.to = to;
        this.cost = cost;
    }
}
class EdgeComparator implements Comparator<Edge> {
    public int compare(Edge one, Edge two) {
        return Integer.compare(one.cost, two.cost);
    }
}
public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        ArrayList<Edge>[] a = new ArrayList[n+1];
        for (int i=1; i<=n; i++) {
            a[i] = new ArrayList<>();
        }
        for (int i=0; i<m; i++) {
            int from = sc.nextInt();
            int to = sc.nextInt();
            int cost = sc.nextInt();
            a[from].add(new Edge(to,cost));
            a[to].add(new Edge(from,cost));
        }
        boolean[] c = new boolean[n+1];
        PriorityQueue<Edge> q = new PriorityQueue<Edge>(1, new EdgeComparator());
        c[1] = true;
        for (Edge e : a[1]) {
            q.add(e);
        }
        int ans = 0;
        while (!q.isEmpty()) {
            Edge e = q.poll();
            if (c[e.to] == true) {
                continue;
            }
            c[e.to] = true;
            ans += e.cost;
            for (Edge ee : a[e.to]) {
                q.add(ee);
            }
        }
        System.out.println(ans);
    }
}
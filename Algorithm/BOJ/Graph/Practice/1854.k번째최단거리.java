import java.util.*;
class Edge implements Comparable<Edge> {
    int to, cost;
    Edge(int to, int cost) {
        this.to = to;
        this.cost = cost;
    }
    public int compareTo(Edge that) {
        if (this.cost < that.cost) {
            return -1;
        } else if (this.cost == that.cost) {
            if (this.to < that.to) return -1;
            else if (this.to > that.to) return 1;
            else return 0;
        } else {
            return 1;
        }
    }
}
public class Main {
    static final int inf = 1000000000;
    static class Compare implements Comparator<Integer> {
        public int compare(Integer one, Integer two) {
            return two.compareTo(one);
        }
    }
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int k = sc.nextInt();
        List<Edge>[] a = (List<Edge>[]) new List[n+1];
        for (int i=1; i<=n; i++) {
            a[i] = new ArrayList<Edge>();
        }
        for (int i=0; i<m; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            int z = sc.nextInt();
            a[x].add(new Edge(y,z));
        }
        PriorityQueue<Integer>[] dist = new PriorityQueue[n+1];
        Compare cmp = new Compare();
        for (int i=1; i<=n; i++) {
            dist[i] = new PriorityQueue<Integer>(1, cmp);
        }
        dist[1].offer(0);
        PriorityQueue<Edge> q = new PriorityQueue<>();
        q.add(new Edge(1, 0));
        while (!q.isEmpty()) {
            Edge p = q.remove();
            int cur = p.cost;
            int x = p.to;
            for (Edge e : a[x]) {
                int y = e.to;
                if (dist[y].size() < k || dist[y].peek() > cur + e.cost) {
                    if (dist[y].size() == k) {
                        dist[y].poll();
                    }
                    dist[y].offer(cur+e.cost);
                    q.add(new Edge(y, (cur+e.cost)));
                }
            }
        }
        for (int i=1; i<=n; i++) {
            if (dist[i].size() != k) {
                System.out.println(-1);
            } else {
                System.out.println(dist[i].peek());
            }
        }
    }
}
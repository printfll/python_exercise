'''
 5 int find_kth(int A[],int m, int B[], int n, int k)
 6 {
 7     if(m > n )  return find_kth(B, n, A, m, k);
 8     if( m == 0) return B[k-1];
 9     if( k == 1) return min(A[0], B[0]);
10 
11     int ia = min(k /2, m);
12     int ib = k -ia;
13     if( A[ia-1] < B[ib -1]) 
14         return find_kth(A +ia, m -ia, B, n, k -ia);
15     else if( A[ia-1] > B[ib-1])
16         return find_kth(A, m, B +ib, n -ib, k -ib);
17     else
18         return A[ia-1];
19 }
20 int main(int argc, char *argv[])
21 {
22     int i,n,m,k;
23     int ans;
24     scanf("%d%d%d",&n,&m,&k);
25     for(i=0;i<n;i++) scanf("%d",&a[i]);
26     for(i=0;i<m;i++) scanf("%d",&b[i]);
27     ans=find_kth(a,n,b,m,k);
28     printf("%d\n",ans);
29     return 0;
30 }
'''

def find_kth(arr_A, arr_B, k):
    print(arr_A, arr_B, k)
    if not arr_A:
        return arr_B[k-1]
    if len(arr_A)>len(arr_B):
        return find_kth(arr_B, arr_A, k)
    if k==1:
        return max(arr_A[0], arr_B[0])
    
    mid = min(k//2, len(arr_A))
    mid_ = k-mid
    mid_A, mid_B = arr_A[mid-1], arr_B[mid_-1]
    if mid_A<mid_B:
        return find_kth(arr_A[mid:], arr_B, k-mid)
    elif mid_A>mid_B:
        return find_kth(arr_A, arr_B[mid_:], k-mid_)
    else:
        return mid_A
    
arr_A=[i+5 for i in range(-30, 20, 5)]
arr_B=[i-3 for i in range(-20, 30, 5)]
sort_C=sorted(arr_A+arr_B)
print(arr_A, arr_B, sort_C)
k=7
print(f"top {k}:{find_kth(arr_A, arr_B, k)}, {sort_C[k]}")
 
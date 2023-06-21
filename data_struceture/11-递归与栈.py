def count_down(i):
  print(i)
  if i<=1:
    return
  count_down(i-1)

if __name__ == "__main__":
    count_down(5)
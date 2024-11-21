
matrix = np.array([[12, -51, 4], [6, 167, -68], [-4, 24, -41]])
Q, R = np.linalg.qr(matrix)
print(f"Q Matrix:\n{Q}\n")
print(f"R Matrix:\n{R}")


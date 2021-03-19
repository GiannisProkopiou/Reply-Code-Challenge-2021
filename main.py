import glob
import parsr, solver, writer

for idx, filename in enumerate(glob.glob('datasets/*')):
    if idx == 1:
        continue

    dataset = parsr.parse(filename)
    print('File: %s' % (filename))

    solution = solver.solve(dataset)
    writer.write(solution, filename.replace('datasets','solutions'))

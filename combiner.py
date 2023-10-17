# this is here to get around github file size limits

import os

print("Combining chunks...")

# Open the output file for writing
with open("badfizzbuzz.py", "wb") as output_file:
    # Loop through the chunk files
    for i in range(100):
        # Generate the filename for the chunk
        filename = os.path.join("chunks", "chunk_" + str(i) + ".py")

        # Check if the chunk file exists
        if os.path.exists(filename):
            # Open the chunk file for reading
            with open(filename, "rb") as chunk_file:
                # Read the chunk from the chunk file
                chunk = chunk_file.read()

                # Write the chunk to the output file
                output_file.write(chunk)
                print(f"Chunk {i} written.")

print("Done re-combining the chunks.")

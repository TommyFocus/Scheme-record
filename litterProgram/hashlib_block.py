import hashlib

class Block:
	def __init__(self, data, prev_hash):
		self.previous_hash = prev_hash
		self.data = data

	@property
	def hash(self):
		message = hashlib.sha256()
		message.update(str(self.data).encode('utf-8'))
		return message.hexdigest()

def create_genesis_block():
	return Block(data="Genesis Block", prev_hash="")

class BlockChain:
	def __init__(self):
		self.blocks = [create_genesis_block()]

	def add_block(self, data):
		prev_block = self.blocks[len(self.blocks) - 1]
		new_block = Block(data, prev_block.hash)
		self.blocks.append(new_block)
		return new_block

if __name__ == '__main__':
	bc = BlockChain()
	b1 = bc.add_block('Jack send 1 BTC to Sam')
	b2 = bc.add_block('Sam send 2 BTC to lill')
	b3 = bc.add_block('Tommy send 34 BTC to Spp')

	for b in bc.blocks:
		print('Prev Hash: {}'.format(b.previous_hash))
		print('Data: {}'.format(b.data))
		print('Hash: {}'.format(b.hash))
		print('-'*100)
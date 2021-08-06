const ParserStateWrapper = require('./ParserStateWrapper')
const Engine = require('./Engine')
const readline = require('readline')

module.exports = class REPLInstigator {
	#engine
	#buffer
	#lineReader

	constructor() {
		this.#engine = new Engine()
		this.#lineReader = readline.createInterface({
		 	input: process.stdin,
		 	output: process.stdout
		})

		this.#readNew()
	}

	#read(cursorStr) {
		this.#lineReader.question(cursorStr, (lineStr) => {
			this.#feedLine(lineStr)
		})
	}

	#readNew() {
		this.#buffer = ''
		this.#read('> ')
	}

	#feedLine(lineStr) {
		this.#buffer += lineStr
		const pw = new ParserStateWrapper()
		const parseResult = pw.parse(this.#buffer)

		switch (parseResult.type) {
			case ParserStateWrapper.Accept:
				this.#handleParsingResult(parseResult.output)
				break

			case ParserStateWrapper.ExpectMore:
				this.#read((this.#buffer.length === 0) ? '> ' : '- ')
				break

			case ParserStateWrapper.Reject:
				console.log('?')
				this.#readNew()
				break
		}
	}
	
	#handleParsingResult(s) {
		try {
			console.log(`${this.#engine.evaluate(s)}`)
		} catch (e) {
			console.log(`Error: ${e.s.car()} - ${e.s.cdr()}`)
		}

		this.#readNew()
	}
}

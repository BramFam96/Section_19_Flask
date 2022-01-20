class BoggleGame {
	/* make a new game at this DOM id */

	constructor(boardId, secs = 60) {
		this.secs = secs // game length
		this.showTimer()

		this.score = 0
		this.words = new Set()
		this.board = $('#' + boardId)

		// every 1000 msec, "tick"
		this.timer = setInterval(this.tick.bind(this), 1000)

		$('.add-word', this.board).on('submit', this.handleSubmit.bind(this))
	}

	/* show word in list of words */

	showWord(word) {
		$('.words', this.board).append($('<li>', { text: word }))
	}

	/* show score in html */

	showScore() {
		$('.score', this.board).text(this.score)
	}

	/* show a status message */

	showMessage(msg, cls) {
		$('.msg', this.board).text(msg).removeClass().addClass(`msg ${cls}`)
	}

	/* handle submission of word: if unique and valid, score & show */

	async handleSubmit(evt) {
		evt.preventDefault()
		const $word = $('.word', this.board)

		let word = $word.val()
		if (!word) return

		if (this.words.has(word)) {
			this.showMessage(`Already found ${word}`, 'err')
			return
		}

		// check server for validity
		const resp = await axios.get('/check-word', { params: { word: word } })
		if (resp.data.result === 'not-word') {
			this.showMessage(`${word} is not a valid English word`, 'err')
		} else if (resp.data.result === 'not-on-board') {
			this.showMessage(`${word} is not a valid word on this board`, 'err')
		} else {
			this.showWord(word)
			this.score += word.length
			this.showScore()
			this.words.add(word)
			this.showMessage(`Added: ${word}`, 'ok')
		}

		$word.val('').focus()
	}

	/* Update timer in DOM */

	showTimer() {
		$('.timer', this.board).text(this.secs)
	}

	/* Tick: handle a second passing in game */

	async tick() {
		this.secs -= 1
		this.showTimer()

		if (this.secs === 0) {
			clearInterval(this.timer)
			await this.scoreGame()
		}
	}

	/* end of game: score and update message. */

	async scoreGame() {
		$('.add-word', this.board).hide()
		const resp = await axios.post('/post-score', { score: this.score })
		if (resp.data.brokeRecord) {
			this.showMessage(`New record: ${this.score}`, 'ok')
		} else {
			this.showMessage(`Final score: ${this.score}`, 'ok')
		}
	}
}
// class BoggleGame {
// 	constructor(boardId, time = 60) {
// 		this.board = $(`#${boardId}`)
// 		this.time = time
// 		this.score = 0
// 		this.words = new Set()
// 		this.showTimer()
// 		this.timer = setInterval(this.tick.bind(this), 1000)
// 		$('.guess', this.board).on('submit', this.handleSubmit.bind(this))
// 	}
// 	// HTML Manipulation:
// 	updateWord(word) {
// 		$('.words', this.board).append($('<li>', { text: word }))
// 	}
// 	updateMsg(msg, cls) {
// 		$('.msg', this.board).text(msg).removeClass().addClass(cls)
// 	}
// 	updateScore() {
// 		$('#score', this.board).text(this.score)
// 	}

// 	//Async funcs:
// 	async handleSubmit(e) {
// 		e.preventDefault()
// 		//  Checking individual word exists;
// 		const $guess = $('.guess', this.board)
// 		let word = $guess.val()
// 		if (!word) return
// 		//Checking for duplicates
// 		if (this.words.has(word)) {
// 			this.updateMsg(`${word} has already been found`, 'err')
// 		}
// 		const res = await axios.get('/handle-guess', { params: { word: word } })
// 		if (res.data.result === 'not-word') {
// 			this.updateMsg(`${word} is not a valid English word`, 'err')
// 		} else if (res.data.result === 'not-on-board') {
// 			this.updateMsg(`${word} is not a valid word on this board`, 'err')
// 		} else {
// 			this.score += word.length
// 			this.showScore()
// 			this.updateWord(word)
// 			this.words.add(word)
// 			this.updateMsg(`Added: ${word}`, 'ok')
// 		}
// 		$guess.val('').focus()
// 	}

// 	/* Update timer in DOM */

// 	showTimer() {
// 		$('.timer', this.board).text(this.time)
// 	}

// 	/* Tick: handle a second passing in game */

// 	async tick() {
// 		this.secs -= 1
// 		this.showTimer()

// 		if (this.secs === 0) {
// 			clearInterval(this.timer)
// 			await this.scoreGame()
// 		}
// 	}

// 	/* end of game: score and update message. */

// 	async scoreGame() {
// 		$('.add-word', this.board).hide()
// 		const resp = await axios.post('/post-score', { score: this.score })
// 		if (resp.data.brokeRecord) {
// 			this.showMessage(`New record: ${this.score}`, 'ok')
// 		} else {
// 			this.showMessage(`Final score: ${this.score}`, 'ok')
// 		}
// 	}
// }

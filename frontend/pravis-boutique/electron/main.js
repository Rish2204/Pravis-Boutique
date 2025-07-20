const { spawn } = require('child_process')
const { app, BrowserWindow } = require('electron')

// Keep a global reference of the window object
let mainWindow
let nuxtProcess

function createWindow () {
  // Create the browser window with macOS optimizations
  mainWindow = new BrowserWindow({
    width: 1400,
    height: 900,
    minWidth: 800,
    minHeight: 600,
    webPreferences: {
      nodeIntegration: false,
      contextIsolation: true,
      enableRemoteModule: false,
      preload: path.join(__dirname, 'preload.js')
    },
    titleBarStyle: 'hiddenInset', // macOS native title bar
    vibrancy: 'under-window', // macOS blur effect
    icon: path.join(__dirname, '../public/icon.png'),
    show: false // Don't show until ready
  })

  // Load the app
  const startUrl = isDev
    ? 'http://localhost:3000'
    : `file://${path.join(__dirname, '../.output/public/index.html')}`

  mainWindow.loadURL(startUrl)

  // Show window when ready to prevent visual flash
  mainWindow.once('ready-to-show', () => {
    mainWindow.show()

    // Focus on the window
    if (isDev) {
      mainWindow.webContents.openDevTools()
    }
  })

  // Handle window closed
  mainWindow.on('closed', () => {
    mainWindow = null
  })

  // Handle external links
  mainWindow.webContents.setWindowOpenHandler(({ url }) => {
    shell.openExternal(url)
    return { action: 'deny' }
  })

  // macOS specific window handling
  mainWindow.on('closed', () => {
    if (process.platform !== 'darwin') {
      app.quit()
    }
  })
}

// Start Nuxt development server
function startNuxtDev () {
  if (isDev) {
    nuxtProcess = spawn('npm', ['run', 'dev'], {
      cwd: path.join(__dirname, '..'),
      stdio: 'pipe'
    })

    nuxtProcess.stdout.on('data', (data) => {
    })

    nuxtProcess.stderr.on('data', (data) => {
    })

    // Wait for Nuxt to start before creating window
    setTimeout(createWindow, 5000)
  } else {
    createWindow()
  }
}

// App event listeners
app.whenReady().then(() => {
  startNuxtDev()

  // Create menu bar (macOS style)
  createMenuBar()

  // macOS dock behavior
  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow()
    }
  })
})

// Quit when all windows are closed
app.on('window-all-closed', () => {
  if (nuxtProcess) {
    nuxtProcess.kill()
  }

  if (process.platform !== 'darwin') {
    app.quit()
  }
})

// Create macOS native menu
function createMenuBar () {
  const template = [
    {
      label: app.getName(),
      submenu: [
        { role: 'about' },
        { type: 'separator' },
        { role: 'services' },
        { type: 'separator' },
        { role: 'hide' },
        { role: 'hideothers' },
        { role: 'unhide' },
        { type: 'separator' },
        { role: 'quit' }
      ]
    },
    {
      label: 'Edit',
      submenu: [
        { role: 'undo' },
        { role: 'redo' },
        { type: 'separator' },
        { role: 'cut' },
        { role: 'copy' },
        { role: 'paste' },
        { role: 'selectall' }
      ]
    },
    {
      label: 'View',
      submenu: [
        { role: 'reload' },
        { role: 'forceReload' },
        { role: 'toggleDevTools' },
        { type: 'separator' },
        { role: 'resetZoom' },
        { role: 'zoomIn' },
        { role: 'zoomOut' },
        { type: 'separator' },
        { role: 'togglefullscreen' }
      ]
    },
    {
      label: 'Window',
      submenu: [
        { role: 'minimize' },
        { role: 'close' },
        { type: 'separator' },
        { role: 'front' }
      ]
    }
  ]

  const menu = Menu.buildFromTemplate(template)
  Menu.setApplicationMenu(menu)
}

// Handle app certificate verification (for dev)
app.on('certificate-error', (event, webContents, url, error, certificate, callback) => {
  if (isDev) {
    event.preventDefault()
    callback(new Error('Certificate error'))
  } else {
    callback(new Error('Certificate error'))
  }
})

# Audio Feedback Assets

This directory contains audio files used for providing auditory feedback to users, especially important for users with visual impairments and to enhance the overall user experience.

## Files and Their Purpose

- `success.mp3` - Played when an action is successfully completed (e.g., adding to cart, completing a purchase)
- `error.mp3` - Played when an error occurs
- `warning.mp3` - Played for warning notifications
- `click.mp3` - Played for general button interactions
- `add-to-cart.mp3` - Played specifically when adding an item to cart
- `notification.mp3` - Played for general notifications and announcements

## Requirements for Audio Files

1. **Duration**: All audio files should be short (0.5-2 seconds) to avoid disrupting the user experience
2. **Format**: Use MP3 format for broad browser compatibility
3. **Volume**: Audio should be normalized to a consistent level
4. **Distinctiveness**: Each sound should be easily distinguishable from others
5. **Subtlety**: Sounds should be subtle and not jarring or annoying

## Accessibility Considerations

- Users should be able to disable audio feedback in their account settings
- Volume levels should be appropriate and not startling
- Audio feedback should always be paired with visual feedback
- Never rely solely on audio to convey critical information

## Adding New Audio Files

When adding new audio files:

1. Keep the file size small (<50KB if possible)
2. Add documentation in this README
3. Update the `audioMap` in `utils/accessibility.js`
4. Test with screen readers to ensure the audio doesn't interfere with screen reader output

## Attribution

All audio files should be either:
- Created specifically for Pravis Boutique
- Licensed under a permissive license (CC0, CC-BY)
- Purchased with appropriate commercial usage rights

Current audio files were sourced from [source] under [license].

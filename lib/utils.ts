import { type ClassValue, clsx } from "clsx"
import { twMerge } from "tailwind-merge"

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}

type ToastType = {
  title: string
  description: string
  variant?: "default" | "destructive"
}

// Simple toast function for notifications
export const toast = ({ title, description, variant = "default" }: ToastType) => {
  console.log(`[${variant.toUpperCase()}] ${title}: ${description}`)
  // In a real app, this would use a toast library or the toast context
  // This is a placeholder implementation
}
 
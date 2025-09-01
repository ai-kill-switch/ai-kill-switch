#!/usr/bin/env python3
"""
Basic Usage Example for AI Kill Switch SDK

Simple test file for the hello function.
"""

from ai_kill_switch import hello

def main():
    """Test the hello function."""
    print("🚀 AI Kill Switch SDK - Basic Test")
    print("=" * 40)
    
    # Test the hello function
    message = hello()
    print(f"Hello function result: {message}")
    
    # Test importing specific function
    from ai_kill_switch import hello as hello_func
    result = hello_func()
    print(f"Direct import result: {result}")
    
    # Test function type
    print(f"Function type: {type(hello)}")
    
    # Test if it's callable
    if callable(hello):
        print("✅ Function is callable")
    else:
        print("❌ Function is not callable")
    
    print("\n✅ Basic test completed!")

if __name__ == "__main__":
    main()

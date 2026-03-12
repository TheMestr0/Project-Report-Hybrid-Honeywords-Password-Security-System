"""
Test runner for honeywords project
Run this file to execute all tests and see comprehensive results
"""

from honeywords import (
    test_honeywords_algorithm,
    test_real_decoys_generator,
    test_merged_system,
    print_final_comments
)

if __name__ == "__main__":
    print("\n" + "#"*70)
    print("# PROJECT #1: HONEYWORDS PASSWORD ALGORITHM")
    print("# Developer: TheMestr0")
    print("# Date: 2026-03-12")
    print("#"*70)
    
    # Test all three components
    test_honeywords_algorithm()
    test_real_decoys_generator()
    test_merged_system()
    
    # Final summary
    print_final_comments()
    
    print("\n" + "#"*70)
    print("# ALL TESTS COMPLETED SUCCESSFULLY")
    print("#"*70 + "\n")